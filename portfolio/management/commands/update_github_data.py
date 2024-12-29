import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from portfolio.models import PerfilModel, FooterModel, ProjetoModel, TecnologiaModel


class Command(BaseCommand):
    help = "Atualiza as informações do banco de dados com os dados da API do GitHub"

    def handle(self, *args, **kwargs):
        user_api_url = "https://api.github.com/users/oOHimuraOo"
        repos_api_url = "https://api.github.com/users/oOHimuraOo/repos"

        try:
            # Requisição para o usuário
            user_response = requests.get(user_api_url)
            user_data = user_response.json()

            # Atualizar ou criar Perfil
            if PerfilModel.objects.exists():
                perfil = PerfilModel.objects.first()
                perfil.image = user_data.get("avatar_url")
                perfil.nick = user_data.get("login")
                perfil.nome_completo = user_data.get("name")
                perfil.email = user_data.get("email")
                perfil.github = user_data.get("html_url")
                perfil.profissao = user_data.get("bio")
                perfil.linkedin = "https://via.placeholder.com/4x4"
                perfil.save()
                self.stdout.write(self.style.SUCCESS(f"Perfil atualizado: {perfil.nome_completo}"))
            else:
                perfil = PerfilModel.objects.create(
                    nick=user_data.get("login"),
                    image=user_data.get("avatar_url"),
                    nome_completo=user_data.get("name"),
                    email=user_data.get("email"),
                    github=user_data.get("html_url"),
                    profissao=user_data.get("bio"),
                    linkedin="https://www.linkedin.com/in/felipe-cerqueira-fernandes-974b4b257/"
                )
                self.stdout.write(self.style.SUCCESS(f"Perfil criado: {perfil.nome_completo}"))

            # Atualizar ou criar Footer
            updated_at = user_data.get("updated_at", None)
            formatted_date = None
            if updated_at:
                try:
                    formatted_date = datetime.fromisoformat(updated_at.rstrip('Z')).strftime('%Y-%m-%d')
                except ValueError:
                    formatted_date = "0000-00-00"  # Valor padrão se o formato for inválido

            if FooterModel.objects.exists():
                footer = FooterModel.objects.first()
                footer.last_update = formatted_date or "0000-00-00"
                footer.views = 1
                footer.author = f'made by {user_data.get("login", "Autor desconhecido")}'
                footer.made_in = 'made with VUE and Django'
                footer.online = True
                footer.save()
                self.stdout.write(self.style.SUCCESS("Footer atualizado com sucesso."))
            else:
                footer = FooterModel.objects.create(
                    last_update=formatted_date or "0000-00-00",
                    views=0,
                    author=f'made by {user_data.get("name", "Autor desconhecido")}',
                    made_in='made with VUE and Django',
                    online=True
                )
                self.stdout.write(self.style.SUCCESS("Footer criado com sucesso."))

            # Garantir tecnologia placeholder
            tecnologia_placeholder, _ = TecnologiaModel.objects.get_or_create(nome="Desconhecida")
            self.stdout.write(self.style.SUCCESS("Tecnologia placeholder garantida."))

            # Requisição para os repositórios
            repos_response = requests.get(repos_api_url)
            repos_data = repos_response.json()

            # Atualizar tabela Tecnologias
            tecnologias = set(repo.get("language") for repo in repos_data if repo.get("language"))
            for tech in tecnologias:
                TecnologiaModel.objects.get_or_create(nome=tech)
            self.stdout.write(self.style.SUCCESS("Tecnologias atualizadas com sucesso."))

            # Atualizar tabela Projetos
            for repo in repos_data:
                linguagem = repo.get("language")
                tecnologia = (
                    TecnologiaModel.objects.filter(nome__iexact=linguagem).first()
                    if linguagem
                    else tecnologia_placeholder
                )

                # Verificar se o projeto já existe
                projeto = ProjetoModel.objects.filter(name=repo.get("name")).first()
                if projeto:
                    # Atualizar somente se necessário
                    has_changes = False
                    if projeto.description != (repo.get("description") or "Descrição não fornecida"):
                        projeto.description = repo.get("description") or "Descrição não fornecida"
                        has_changes = True
                    if projeto.tecnologia != tecnologia:
                        projeto.tecnologia = tecnologia
                        has_changes = True
                    if has_changes:
                        projeto.save()
                        self.stdout.write(self.style.SUCCESS(f"Projeto atualizado: {projeto.name}"))
                else:
                    projeto = ProjetoModel.objects.create(
                        name=repo.get("name"),
                        description=repo.get("description") or "Descrição não fornecida",
                        conclusion="Conclusão pendente",
                        code_ex="Código exemplo pendente",
                        url=repo.get("html_url"),
                        icon="https://via.placeholder.com/5x5",
                        tecnologia=tecnologia
                    )
                    self.stdout.write(self.style.SUCCESS(f"Projeto criado: {projeto.name}"))

        except requests.RequestException as e:
            self.stderr.write(f"Erro ao acessar a API do GitHub: {e}")
        except Exception as e:
            self.stderr.write(f"Erro geral: {e}")
