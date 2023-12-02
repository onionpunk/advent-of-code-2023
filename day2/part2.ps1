$sumPower = 0

Get-Content .\input.txt | % {
    $line = $_
    $line -match "Game (?<gameNum>.+): (?<gameResults>.+)" | out-null
    $gameNum = [int]$Matches["gameNum"]
    $gameResults =  $Matches["gameResults"] -split ";"
    $maxGreen = 0
    $maxRed = 0
    $maxBlue = 0
    $gameResults.trim() | % {
        $gameRound = $_ -split ","
        $gameRound | % {
            $colourResult = $_.trim()
            $colourResult -match "(?<quantity>.+) (?<colour>.+)" | out-null
            $quantity = [int]$Matches["quantity"]
            $colour = $Matches["colour"].ToLower()
            if ( ($colour -eq "green") -and ($maxGreen -lt $quantity) ) {
                $maxGreen = $quantity
            }
            elseif ( ($colour -eq "red") -and ($maxRed -lt $quantity) ) {
                $maxRed = $quantity
            }
            elseif ( ($colour -eq "blue") -and ($maxBlue -lt $quantity) ) {
                $maxBlue = $quantity
            }
        }
    }

    $sumPower += $maxGreen * $maxRed * $maxBlue
}

$sumPower