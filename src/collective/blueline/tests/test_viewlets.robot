*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Variables  plone/app/testing/interfaces.py

Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close all browsers

*** Variables ***

${site_setup}  ${PLONE_URL}/@@overview-controlpanel
${blueline_configlet}  ${PLONE_URL}/@@blueline-settings
${diazo_configlet}  ${PLONE_URL}/@@theming-controlpanel
${page}  ${PLONE_URL}/title-1
${show_authenticated_locator}  css=#form-widgets-show_authenticated-0
${head_locator}  css=#form-widgets-html_head
${image}  <img src="\${context/@@plone_portal_state/portal_url}/logo.png" />
${evaluated_image_locator}  css=body > img[src=http\\:\\/\\/localhost\\:55001\\/plone\\/logo\\.png]
${header_locator}  css=#form-widgets-header
${script}  <script>document.write('Hello' + ' ' + 'World!')</script>
${message}  Hello World!
${abovecontent_locator}  css=#form-widgets-above_content
${belowcontent_locator}  css=#form-widgets-below_content
${conditional1}  <span tal:condition="python:context.absolute_url().endswith('plone')" tal:omit-tag="">Root page1</span>
${conditional2}  <script> if ('\${context/Title}' === 'Plone site') { document.write('Root' + ' ' + 'page2'); } </script> 
${conditional1_message}  Root page1
${conditional2_message}  Root page2

*** Keywords ***

Goto Blueline Configlet
    Go to  ${blueline_configlet}
    Page Should Contain  Blueline

Goto Diazo Configlet
    Go to  ${diazo_configlet}
    Page Should Contain  Theme settings

Goto Page
    Go to  ${page}
    Page Should Contain  Title

Populate Viewlet
    Goto Blueline Configlet
    Input Text  ${head_locator}  ${image}
    Input Text  ${header_locator}  ${script}
    Input Text  ${abovecontent_locator}  ${conditional1}
    Input Text  ${belowcontent_locator}  ${conditional2}
    Click Button  Save

Enable Show to Authenticated
    Goto Blueline Configlet
    Select Checkbox  ${show_authenticated_locator}
    Click Button  Save

Add One Page
    Goto Homepage
    Open Add New Menu
    Click Link  css=a#document
    Page Should Contain  Add Page
    Input Text  css=#title  Title
    Click Button  Save


*** Test cases ***

Test Configlet
    Enable Autologin as  Manager
    Go to  ${site_setup}
    Page Should Contain  Blueline

Test Viewlets as Authenticated
    Enable Autologin as  Manager
    Populate Viewlet

    # viewlet code should not be visible to authenticated users by default
    Go to Homepage
    Page Should Not Contain Element  ${evaluated_image_locator}
    Page Should Not Contain  ${message}

    # Add new page
    Add One Page

    # make it visible
    Enable Show to Authenticated
    Go to Homepage
    Page Should Contain Element  ${evaluated_image_locator}
    Page Should Contain  ${message}
    Page Should Contain  ${conditional1_message}
    Page Should Contain  ${conditional2_message}

    # conditionals should not be visible outside root page
    Goto Page
    Page Should Contain Element  ${evaluated_image_locator}
    Page Should Contain  ${message}
    Page Should Not Contain  ${conditional1_message}
    Page Should Not Contain  ${conditional2_message}

    # viewlets should not be visible in the context of some configlets
    Goto Blueline Configlet
    Page Should Not Contain Element  ${evaluated_image_locator}
    Page Should Not Contain  ${message}
    Goto Diazo Configlet
    Page Should Not Contain Element  ${evaluated_image_locator}
    Page Should Not Contain  ${message}


Test Viewlets as Anonymous
    Enable Autologin as  Manager
    Populate Viewlet
    Disable Autologin
    Go to Homepage
    Page Should Contain Element  ${evaluated_image_locator}
    Page Should Contain  ${message}
