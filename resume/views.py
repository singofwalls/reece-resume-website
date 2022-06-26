from collections import namedtuple
from django.http import HttpResponse
from django.views.generic import TemplateView


Project = namedtuple("Project", "title type desc img url components")
Experience = namedtuple("Experience", "title location address supervisor desc components period")

class index(TemplateView):
    projects = [
        Project("CourseCorrect", 
                "Class Group Project", "A course planner with a drag and drop UI for deciding when to take classes and an administrator interface for creating new classes and degree requirements.", 
                "https://coursecorrect.pericarpal.com/images/logo.png", 
                "https://coursecorrect.pericarpal.com/",
                ["PHP", "JS", "CSS", "Bootstrap", "HTML", "Apache", "Ubuntu", "WSL", "Webhosting", "MySQL", "DNS"]),
        Project("Stravan't", 
                "Class Group Project", 
                "An activity tracker and social media site to share activities with GPS map support.", 
                "https://stravant.pericarpal.com/logo.png", 
                "https://stravant.pericarpal.com/",
                ["PHP", "JS", "CSS", "Bootstrap", "HTML", "Apache", "Ubuntu", "WSL", "Webhosting", "MySQL", "DNS"]),
        Project("GMod TTT Role Descriptions Menu", 
                "Personal Project", 
                "A utility addon for the TTT gamemode of the video game, Garry's Mod, adding a menu to explain character objectives to new users.", 
                "https://raw.githubusercontent.com/singofwalls/gmod_ttt2_role_menu/master/role_menu.jpg", 
                "https://github.com/singofwalls/gmod_ttt2_role_menu",
                ["Lua", "Opensource"]),
        Project("Lyrics Tweeter", 
                "Personal Project", 
                "A Twitter bot which occasionally tweets out random lyrics from the song I am currently listening to on Spotify.", 
                "", 
                "https://github.com/singofwalls/Lyrics-Tweeter",
                ["Python", "Web APIs", "Twitter Bots", "Ubuntu"]),
        Project("Odyssey Text Adventure", 
                "Class Project", 
                "A text-based adventure game with a GUI and hotkey support.", 
                "", 
                "https://github.com/singofwalls/Odyssey-Text-Adventure",
                ["Python", "Pygame", "GUIs"]),
    ]
    experiences = [
        Experience("Research Assistant", 
            "The Center for Remote Sensing of Ice Sheets <br><small>(CReSIS), University of Kansas</small>", 
            "2335 Irving Hill Road, Lawrence, Kansas 66045",
            "Dr. John Paden",
            "Upgraded a web-application's entire stack including the server hardware, OS, database, backend code, and frontend code. Adding features to Matlab and Django code bases.", 
            ["Matlab", "Django", "Python", "Postgresql", "CentOS", "Linux", "Machine Learning", "JS", "GeoServer", "Webhosting", "Apache"],
            "2019 - Present"),
        Experience("IT Lead", 
            "American Legion Boys State of Kansas", 
            "1314 SW. Topeka Blvd., Topeka, KS 66612",
            "Trey Scarborough",
            "Maintaining and upgrading the economy simulation used by the Kansas Boys State program to provide an interactive experience to the participants during the annual week-long session. Writing scripts to automate various IT tasks. Imaging computers.", 
            ["Python", "C#", "Microsoft Access", "Azure", "Windows", "ChromeOS", "Ubuntu"],
            "2018 - Present"),
        Experience("IT Intern", 
            "K•Coe Isom", 
            "3030 Cortland Cir., Salina, KS 67401",
            "Bill Woolsey",
            "Automated several tasks with Powershell and AutoIt with extensive logging. Researched options to determine the best products for the firm to incorporate.", 
            ["Powershell", "AutoIt", "AutoHotkey", "RegEx", "Windows"],
            "2017 - 2018"),
        Experience("Utility Intern", 
            "The Land Institute", 
            "2440 E Water Well Rd, Salina, Kansas 67401",
            "Dr. Tim Crews",
            "Rewrote GUI for an aerodynamic analyzer in Python with Pyglet and OpenGL to display a real time count of seeds accumulating in a series of bins by interfacing with a NI DAQ device.", 
            ["Python", "Pyglet", "NI-DAQ"],
            "2017 - 2018"),
    ]
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.projects
        context['experiences'] = self.experiences
        return context