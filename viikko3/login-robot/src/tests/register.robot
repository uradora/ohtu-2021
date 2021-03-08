*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  meri  merimer0
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Create User  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Create User  mr  purjopor4
    Output Should Contain  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Create User  merir  mer
    Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  merir  merimeri
    Output Should Contain  Password must contain at least one numeric character

