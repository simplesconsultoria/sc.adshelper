# -*- coding: utf-8 -*-
from collective.blueline.portlets import blueline as bluelineprofile
from collective.blueline.testing import INTEGRATION_TESTING
from plone.app.portlets.storage import PortletAssignmentMapping
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility, getMultiAdapter

import unittest


HTML = (
    u'<script>'
    u'  var html = document.createElement("div");'
    u'  html.innerHTML = "TEST";'
    u'  document.body.appendChild(divtest);'
    u'</script>'
)


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
        portlet = bluelineprofile.Assignment(
            embed=HTML,
            title=u'Test',
            description=u'Testing'
        )

        self.assertTrue(IPortletAssignment.providedBy(portlet))
        self.assertTrue(IPortletDataProvider.providedBy(portlet.data))

    def test_invoke_add_view(self):
        name = 'collective.blueline'
        portlet = getUtility(IPortletType, name=name)
        mapping = self.portal.restrictedTraverse('++contextportlets++plone.leftcolumn')

        for m in mapping.keys():
            del mapping[m]

        addview = mapping.restrictedTraverse('+/' + portlet.addview)

        addview.createAndAdd(data=dict(
            embed=HTML,
            title=u'Test',
            description=u'Testing'
        ))

        self.assertEqual(len(mapping), 1)
        self.assertIsInstance(mapping.values()[0], bluelineprofile.Assignment)

    def test_invoke_edit_view(self):
        mapping = PortletAssignmentMapping()
        request = self.request

        mapping['foo'] = bluelineprofile.Assignment(
            embed=HTML,
            title=u'Test',
            description=u'Testing'
        )

        editview = getMultiAdapter((mapping['foo'], request), name='edit')
        self.assertIsInstance(editview, bluelineprofile.EditForm)

    def test_obtain_renderer(self):
        context = self.portal
        request = self.request
        view = context.restrictedTraverse('@@plone')
        manager = getUtility(
            IPortletManager, name='plone.rightcolumn', context=self.portal)

        assignment = bluelineprofile.Assignment(
            embed=HTML,
            title=u'Test',
            description=u'Testing'
        )

        renderer = getMultiAdapter(
            (context, request, view, manager, assignment), IPortletRenderer)

        self.assertIsInstance(renderer, bluelineprofile.Renderer)


class RenderTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def renderer(
        self, context=None, request=None, view=None, manager=None, assignment=None
    ):
        if context is None:
            context = self.portal
        if request is None:
            request = self.request
        if view is None:
            view = self.portal.restrictedTraverse('@@plone')
        if manager is None:
            manager = getUtility(
                IPortletManager,
                name='plone.rightcolumn',
                context=self.portal
            )
        if assignment is None:
            assignment = bluelineprofile.Assignment()

        return getMultiAdapter(
            (context, request, view, manager, assignment), IPortletRenderer)

    def test_render(self):
        assignment = bluelineprofile.Assignment(
            embed=HTML,
            title=u'Test',
            description=u'Testing'
        )
        r = self.renderer(context=self.portal, assignment=assignment)
        r = r.__of__(self.portal)
        r.update()
        output = r.render()

        self.assertIn('<h3 class="portlet-blueline-title">Test</h3>', output)
        self.assertIn('html.innerHTML = "TEST";', output)
