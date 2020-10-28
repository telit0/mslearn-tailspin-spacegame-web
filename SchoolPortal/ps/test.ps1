function test_script {
    param (

    [string]$Token,

    [string]$Username
    )
    
    $Data= [PSCustomObject]@{
        Name = $Username
        Token = $Token
    }

    $Data | export-csv outfile.csv -notypeinformation -append
}

test_script -token "asdf adasdf af" -username "telito"