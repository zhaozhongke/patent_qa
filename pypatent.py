from patent_client import Inpadoc, Assignment, USApplication
app = USApplication.objects.get('15710770')
app.patent_title