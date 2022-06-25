from collections import namedtuple
from django.http import HttpResponse
from django.views.generic import TemplateView


Project = namedtuple("Project", "title type desc img url")

class index(TemplateView):
    projects = [
        Project("CourseCorrect", "Class Project", "A course planner with a drag and drop UI for deciding when to take classes and an administrator interface for creating new classes and degree requirements", "https://coursecorrect.pericarpal.com/images/logo.png", "https://coursecorrect.pericarpal.com/"),
        Project("Stravan't", "Class Project", "An activity tracker and social media site to share activities with GPS map support", "https://stravant.pericarpal.com/logo.png", "https://stravant.pericarpal.com/"),
        Project("GMod TTT Role Descriptions Menu", "Personal Project", "A utility addon for the TTT gamemode of the video game, Garry's Mod, adding a menu to explain character objectives to new users", "https://raw.githubusercontent.com/singofwalls/gmod_ttt2_role_menu/master/role_menu.jpg", "https://github.com/singofwalls/gmod_ttt2_role_menu"),
    ]
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.projects
        return context