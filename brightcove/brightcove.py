"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment


class BrightcoveXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    id = String(display_name="Video ID",
                  default="AQ~~,AAAA1oy1bvE~,ALl2ezBj3WG3MLvDx9F9zkV06cNK00ey",
                  scope=Scope.content,
                  help="Video id that will be shown in the XBlock")
    player_id = String(display_name="Video ID",
                  default="922656010001",
                  scope=Scope.content,
                  help="Player Id that will be shown in the XBlock")

    display_name = String(display_name="Display Name",
                          default="Brightcove Video",
                          scope=Scope.settings,
                          help="Name of the component in the edxplatform")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the BrightcoveXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/brightcove.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/brightcove.css"))
        frag.add_javascript(self.resource_string("static/js/src/brightcove.js"))
        frag.initialize_js('BrightcoveXBlock')
        return frag
        
    def studio_view(self, context=None):
        """
        The primary view of the paellaXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/brightcove_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/brightcove_edit.js"))
        frag.initialize_js('brightcoveXBlock')
        return frag

    @XBlock.json_handler
    def save_pdf(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        self.id = data['id']
        self.player_id = data['player_id']
        self.display_name = data['display_name']

        return {
            'result': 'success',
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("BrightcoveXBlock",
             """<brightcove/>
             """),
            ("Multiple BrightcoveXBlock",
             """<vertical_demo>
                <brightcove/>
                <brightcove/>
                <brightcove/>
                </vertical_demo>
             """),
        ]
