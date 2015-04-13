*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Variables  plone/app/testing/interfaces.py
Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close all browsers

*** Variables ***

${site_setup}  ${PLONE_URL}/@@overview-controlpanel
${blueline_configlet}  ${PLONE_URL}/@@blueline-settings
${show_authenticated_locator}  css=#form-widgets-show_authenticated-0
${header_locator}  css=#form-widgets-header
${script}  <script>document.write('Hello' + ' ' + 'World!')</script>
${message}  Hello World!

*** Test cases ***

Test Configlet
    Enable Autologin as  Manager
    Go to  ${site_setup}
    Page Should Contain  Blueline

Test Viewlets
    Enable Autologin as  Manager
    Go to  ${blueline_configlet}
    Page Should Contain  Blueline

    # viewlet code should not be visible to authenticated users by default
    Input Text  ${header_locator}  ${script}
    Click Button  Save
    Go to Homepage
    Page Should Not Contain  ${message}

    # make it visible
    Go to  ${blueline_configlet}
    Select Checkbox  ${show_authenticated_locator}
    Click Button  Save
    Go to Homepage
    Page Should Contain  ${message}

    Logout
    Page Should Contain  ${message}
