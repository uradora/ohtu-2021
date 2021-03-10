*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testicase
    Set Password  testicase0
    Set Password Confirmation  testicase0
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testicase1
    Set Password Confirmation  testicase1
    Submit Register
    Register Should Fail With Message  Username must be at least 3 characters

*** Keywords ***
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

