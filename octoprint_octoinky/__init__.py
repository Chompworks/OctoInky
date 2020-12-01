# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
from inky.auto import auto
from PIL import Image

inky = auto()
inky.setup()

class OctoInkyPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        startup_image = Image.open(os.path.join(PATH, "static/img/phat/startup.png"))
        inky.set_image(startup_image)
        inky.show(busy_wait=False)
        self._logger.info("Inky PHAT should be initialised!")
        
#TODO
#test this works!
#create B&W, B&W&R, B&W&R image for startup
#start handling states and creating images using PIL
