# -*- coding: utf-8 -*-

import unittest

from zope.component import getUtility, getMultiAdapter

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.portlets.interfaces import IPortletType
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletRenderer
from plone.app.portlets.storage import PortletAssignmentMapping

from collective.blueline.testing import INTEGRATION_TESTING
from collective.blueline.portlets import blueline as bluelineprofile


class PortletTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_portlet_type_registered(self):
        name = 'collective.blueline'
        portlet = getUtility(IPortletType, name=name)
        self.assertEqual(portlet.addview, name)

    def test_interfaces(self):
        portlet = bluelineprofile.Assignment(embed=u"""<script>
                                                          var html = document.createElement('div');
                                                          html.innerHTML = 'TEST';
                                                          document.body.appendChild(divtest);
                                                       </script>""",
                                             title=u"Test",
                                             description=u"Testing")

        self.assertTrue(IPortletAssignment.providedBy(portlet))
        self.assertTrue(IPortletDataProvider.providedBy(portlet.data))

    def test_invoke_add_view(self):
        name = 'collective.blueline'
        portlet = getUtility(IPortletType, name=name)
        mapping = self.portal.restrictedTraverse('++contextportlets++plone.leftcolumn')

        for m in mapping.keys():
            del mapping[m]

        addview = mapping.restrictedTraverse('+/' + portlet.addview)

        addview.createAndAdd(data={'embed': u"""<script>
                                                  var html = document.createElement('div');
                                                  html.innerHTML = 'TEST';
                                                  document.body.appendChild(divtest);
                                                </script>""",
                                   'title': u"Test",
                                   'description': u"Testing"})

        self.assertEqual(len(mapping), 1)
        self.assertTrue(isinstance(mapping.values()[0],
                                   bluelineprofile.Assignment))

    def test_invoke_edit_view(self):
        mapping = PortletAssignmentMapping()
        request = self.request

        mapping['foo'] = bluelineprofile.Assignment(embed=u"""<script>
                                                                var html = document.createElement('div');
                                                                html.innerHTML = 'TEST';
                                                                document.body.appendChild(divtest);
                                                              </script>""",
                                                    title=u"Test",
                                                    description=u"Testing")

        editview = getMultiAdapter((mapping['foo'], request), name='edit')
        self.assertTrue(isinstance(editview, bluelineprofile.EditForm))

    def test_obtain_renderer(self):
        context = self.portal
        request = self.request
        view = context.restrictedTraverse('@@plone')
        manager = getUtility(IPortletManager, name='plone.rightcolumn',
                             context=self.portal)

        assignment = bluelineprofile.Assignment(embed=u"""<script>
                                                            var html = document.createElement('div');
                                                            html.innerHTML = 'TEST';
                                                            document.body.appendChild(divtest);
                                                          </script>""",
                                                title=u"Test",
                                                description=u"Testing")

        renderer = getMultiAdapter(
            (context, request, view, manager, assignment), IPortletRenderer)

        self.assertTrue(isinstance(renderer,
                                   bluelineprofile.Renderer))


class RenderTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def renderer(self, context=None, request=None, view=None, manager=None,
                 assignment=None):
        context = context or self.portal
        request = request or self.request
        view = view or self.portal.restrictedTraverse('@@plone')
        manager = manager or getUtility(IPortletManager,
                                        name='plone.rightcolumn',
                                        context=self.portal)

        assignment = assignment or bluelineprofile.Assignment()
        return getMultiAdapter((context, request, view, manager, assignment),
                               IPortletRenderer)

    def test_render(self):
        r = self.renderer(context=self.portal,
                          assignment=bluelineprofile.Assignment(embed=u"""<script>
                                                                            var html = document.createElement('div');
                                                                            html.innerHTML = 'TEST';
                                                                            document.body.appendChild(divtest);
                                                                          </script>""",
                                                                title=u"Test",
                                                                description=u"Testing"))
        r = r.__of__(self.portal)
        r.update()
        output = r.render()

        self.assertTrue('<h3 class="portlet-blueline-title">Test</h3>' in output)
        self.assertTrue('html.innerHTML = \'TEST\';' in output)
