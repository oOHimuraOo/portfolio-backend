import os
import json
from django.core.management.base import BaseCommand
from portfolio.models import (
    CursoModel,
    SubProjetoModel,
    ProjetoModel,
    TecnologiaModel,
    EscolasModel,
)


class Command(BaseCommand):
    help = "Processa informações do arquivo JSON e atualiza o banco de dados com verificações detalhadas."

    STATUS_MAP = {
        "completed": 0,
        "incomplete": 1,
        "dropped": 2,
    }

    def handle(self, *args, **kwargs):
        json_file = "./portfolio/management/commands/remaining_info.json"  # Caminho do JSON

        if not os.path.exists(json_file):
            self.stderr.write("Arquivo JSON 'remaining_info.json' não encontrado!")
            return

        try:
            # Ler o JSON
            with open(json_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Processar as informações
            self.process_schools(data)
            self.process_technologies(data)
            self.process_courses(data)
            self.process_projects_and_subprojects(data)

        except Exception as e:
            self.stderr.write(f"Erro ao processar o JSON: {e}")

    # --- Processar Escolas ---
    def process_schools(self, data):
        self.stdout.write("Processando Escolas...")
        for curso in data.get("cursos", {}).values():
            school_name = curso.get("escola")
            if not school_name:
                continue

            # Verificar se a escola já existe
            if EscolasModel.objects.filter(name=school_name).exists():
                self.stdout.write(f"Escola '{school_name}' já registrada.")
            else:
                EscolasModel.objects.create(name=school_name)
                self.stdout.write(f"Escola registrada: {school_name}")

    # --- Processar Tecnologias ---
    def process_technologies(self, data):
        self.stdout.write("Processando Tecnologias...")
        technologies = set()

        # Coletar tecnologias dos cursos, projetos e subprojetos
        for curso in data.get("cursos", {}).values():
            tech_name = curso.get("tecnologia")
            if tech_name:
                technologies.add(tech_name)

        for projeto in data.get("Projetos", {}).values():
            tech_name = projeto.get("tecnologia")
            if tech_name:
                technologies.add(tech_name)

            for subprojeto in projeto.get("subprojetos", {}).values():
                tech_name = subprojeto.get("tecnologia")
                if tech_name:
                    technologies.add(tech_name)

        # Verificar e registrar tecnologias
        for tech_name in technologies:
            if TecnologiaModel.objects.filter(nome=tech_name).exists():
                self.stdout.write(f"Tecnologia '{tech_name}' já registrada.")
            else:
                TecnologiaModel.objects.create(nome=tech_name)
                self.stdout.write(f"Tecnologia registrada: {tech_name}")

    # --- Processar Cursos ---
    def process_courses(self, data):
        self.stdout.write("Processando Cursos...")
        for curso in data.get("cursos", {}).values():
            curso_name = curso.get("name")
            if CursoModel.objects.filter(nome=curso_name).exists():
                self.stdout.write(f"Curso '{curso_name}' ignorado por repetição.")
                continue

            # Registrar curso
            escola = EscolasModel.objects.filter(name=curso.get("escola")).first()
            tecnologia = TecnologiaModel.objects.filter(nome=curso.get("tecnologia")).first()

            CursoModel.objects.create(
                nome=curso_name,
                icon=curso.get("icon", "https://via.placeholder.com/150"),
                codigo_cert=curso.get("Code_cert", "Não fornecido"),
                status=self.STATUS_MAP.get(curso.get("status", "incomplete"), 1),
                descricao=curso.get("descricao", "Sem descrição"),
                url=curso.get("url", "https://via.placeholder.com"),
                escola=escola,
                tecnologia=tecnologia,
            )
            self.stdout.write(f"Curso registrado: {curso_name}")

    # --- Processar Projetos e Subprojetos ---
    def process_projects_and_subprojects(self, data):
        self.stdout.write("Processando Projetos e Subprojetos...")
        for projeto_data in data.get("projetos", {}).values():
            projeto_name = projeto_data.get("name")
            projeto = ProjetoModel.objects.filter(name=projeto_name).first()

            
            # Verificar se o projeto existe no banco
            if not projeto:
                self.stdout.write(f"Projeto '{projeto_name}' inexistente na tabela projetos. Ignorado.")
                continue
            
            # Verificar mudanças no projeto
            has_changes = False
            if projeto.conclusion != projeto_data.get("conclusion", "Conclusão pendente"):
                projeto.conclusion = projeto_data.get("conclusion", "Conclusão pendente")
                has_changes = True
            if projeto.code_ex != projeto_data.get("code_ex", "Nenhum exemplo fornecido"):
                projeto.code_ex = projeto_data.get("code_ex", "Nenhum exemplo fornecido")
                has_changes = True
            if projeto.icon != projeto_data.get("icon", "https://via.placeholder.com/150"):
                projeto.icon = projeto_data.get("icon", "https://via.placeholder.com/150")
                has_changes = True
            if projeto.status != self.STATUS_MAP.get(projeto_data.get("status", "incomplete"), 1):
                projeto.status = self.STATUS_MAP.get(projeto_data.get("status", "incomplete"), 1)
                has_changes = True

            if has_changes:
                projeto.save()
                self.stdout.write(f"Projeto '{projeto_name}' atualizado com alterações.")
            else:
                self.stdout.write(f"Projeto '{projeto_name}' ignorado por falta de modificações.")

            # Processar subprojetos
            for subprojeto_data in projeto_data.get("subprojetos", {}).values():
                subprojeto_name = subprojeto_data.get("name")
                existing_subproject = SubProjetoModel.objects.filter(name=subprojeto_name).first()

                if existing_subproject:
                    # Verificar mudanças no subprojeto
                    has_changes = False
                    if existing_subproject.description != subprojeto_data.get("description", "Sem descrição"):
                        existing_subproject.description = subprojeto_data.get("description", "Sem descrição")
                        has_changes = True
                    if existing_subproject.conclusion != subprojeto_data.get("conclusion", "Conclusão pendente"):
                        existing_subproject.conclusion = subprojeto_data.get("conclusion", "Conclusão pendente")
                        has_changes = True
                    if existing_subproject.code_ex != subprojeto_data.get("code_ex", "Nenhum exemplo fornecido"):
                        existing_subproject.code_ex = subprojeto_data.get("code_ex", "Nenhum exemplo fornecido")
                        has_changes = True
                    if existing_subproject.tecnologia != subprojeto_data.get("Tecnologia", "Desconhecida"):
                        existing_subproject.tecnologia = TecnologiaModel.objects.filter(nome=subprojeto_data.get("Tecnologia")).first()
                        has_changes = True

                    if has_changes:
                        existing_subproject.save()
                        self.stdout.write(f"Subprojeto '{subprojeto_name}' atualizado com alterações.")
                    else:
                        self.stdout.write(f"Subprojeto '{subprojeto_name}' ignorado por falta de modificações.")
                else:
                    # Criar novo subprojeto
                    SubProjetoModel.objects.create(
                        name=subprojeto_name,
                        description=subprojeto_data.get("description", "Sem descrição"),
                        conclusion=subprojeto_data.get("conclusion", "Conclusão pendente"),
                        code_ex=subprojeto_data.get("code_ex", "Nenhum exemplo fornecido"),
                        status=self.STATUS_MAP.get(subprojeto_data.get("status", "incomplete"), 1),
                        icon=subprojeto_data.get("icon", "https://via.placeholder.com/150"),
                        tecnologia=TecnologiaModel.objects.filter(nome=subprojeto_data.get("Tecnologia")).first(),
                        projeto=projeto,
                    )
                    self.stdout.write(f"Subprojeto '{subprojeto_name}' registrado.")
