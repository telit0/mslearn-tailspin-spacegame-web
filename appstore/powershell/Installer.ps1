param (

    $Token,
    $ExpiresAt,
    $AppInfo
    )

    $authHeader = @{
        'Content-Type'='application/json'
        'Authorization'="Bearer " + $Token
        'ExpiresOn'=$ExpiresaAt
        }

        #CleanUp
        $AppInfo=$appInfo -replace '''','"'
        $AppInfo=$appInfo -replace '""','"'
        #$AppInfo=$appInfo -replace 'True','"True"'
        #$AppInfo=$appInfo -replace 'False','"False"'
        $App=$appInfo | ConvertFrom-Json
        $app | export-csv c:\ps\app.csv -notypeinformation -Append -Force