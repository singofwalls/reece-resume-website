from collections import Counter, namedtuple
from itertools import chain
from django.http import HttpResponse
from django.views.generic import TemplateView


Project = namedtuple("Project", "title type desc img url components")
Experience = namedtuple("Experience", "title location address supervisor desc components period")
Social = namedtuple("Social", "name icon user url")

class index(TemplateView):
    projects = [
        Project("Résumé Website", 
                "Personal Project", 
                "This website is built in Django, using Bootstrap for frontend styling. It is hosted on an Ubuntu server running Apache on my local network, proxied through Cloudflare.", 
                "", 
                "https://github.com/singofwalls/reece-resume-website",
                ["Python", "Django", "JS", "CSS", "Bootstrap", "HTML", "Apache", "Ubuntu", "Webhosting", "DNS", "Cloudflare", "Webdesign"]),
        Project("CourseCorrect", 
                "Class Group Project", "A course planner with a drag and drop UI for deciding when to take classes and an administrator interface for creating new classes and degree requirements.", 
                "https://coursecorrect.pericarpal.com/images/logo.png", 
                "https://coursecorrect.pericarpal.com/",
                ["PHP", "JS", "CSS", "Bootstrap", "HTML", "Apache", "Ubuntu", "WSL", "Webhosting", "MySQL", "DNS", "Webdesign"]),
        Project("Stravan't", 
                "Class Group Project", 
                "An activity tracker and social media site to share activities with GPS map support.", 
                "https://stravant.pericarpal.com/logo.png", 
                "https://stravant.pericarpal.com/",
                ["PHP", "JS", "CSS", "Bootstrap", "HTML", "Apache", "Ubuntu", "WSL", "Webhosting", "MySQL", "DNS", "Webdesign"]),
        Project("Tabletop RPG Level Counter", 
                "Personal Project", 
                "A level and stat tracker for the Steve Jackson Games tabletop game, <i>Munchkin</i>.", 
                "", 
                "https://github.com/singofwalls/Table-Top-RPG-Level-Counter",
                ["Python", "Pygame", "GUIs"]),
        Project("Google Drive Scrub", 
                "Personal Project", 
                "A utility script for copying the structure of a Google Drive directory to a YAML file and to reproduce Google Drive directories from YAML files, maintaining permissions of subfolders but emptying the contents.", 
                "", 
                "https://github.com/singofwalls/GoogleDriveScrub",
                ["Python", "Google Drive API", "Automation"]),
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
        Experience("Computer Science Student", 
            "University of Kansas", 
            "1450 Jayhawk Blvd, Lawrence, KS 66045",
            "",
            "Bachelors of Science in Computer Science", 
            ["Matlab", "C++", "Python", "MySQL", "Linux", "Haskell", "Machine Learning", "JS", "x64 Assembly", "MIPS Assembly", "Interpreters", "Compilers"],
            "2018 - 2022"),
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
            "2018"),
        Experience("Utility Intern", 
            "The Land Institute", 
            "2440 E Water Well Rd, Salina, Kansas 67401",
            "Dr. Tim Crews",
            "Rewrote GUI for an aerodynamic analyzer in Python with Pyglet and OpenGL to display a real time count of seeds accumulating in a series of bins by interfacing with a NI DAQ device.", 
            ["Python", "Pyglet", "NI-DAQ"],
            "2017"),
    ]
    socials = [
        Social("Email", 
               "logos/email.png",
               "reece@pericarpal.com",
               "mailto:reece@pericarpal.com"),
        Social("Github", 
               "logos/GitHub-Mark-Light-120px-plus.png",
               "singofwalls",
               "https://github.com/singofwalls"),
        Social("Stack Overflow", 
               "logos/LogoGlyphXxs.png",
               "reece-mathews",
               "https://stackoverflow.com/users/7587147/reece-mathews"),
        Social("Twitter", 
               "logos/Twitter social icons - circle - white.png",
               "singofwalls",
               "https://twitter.com/singofwalls"),
        Social("Linked In", 
               "logos/linkedin.png",
               "reece-mathews",
               "https://linkedin.com/in/reece-mathews"),
    ]

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.projects
        context['experiences'] = self.experiences
        context['socials'] = self.socials

        # Consolidate skills
        skills = list(chain.from_iterable([project.components for project in self.projects]))
        skills += list(chain.from_iterable([experience.components for experience in self.experiences]))
        # Sort by frequency
        skills = Counter(skills)
        context["skills"] = sorted(skills.keys(), key=lambda skill: skills[skill], reverse=True)


        return context