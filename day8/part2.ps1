$file = Get-content "./input.txt"

$instruction = $file[0]

$startingKeysSteps = @()
$startingKeys = @()
$nodes = @{}

2..$file.Length | % {
    $line = $file[$_]
    $line -match "(?<node>.+) = \((?<left>.+), (?<right>.+)\)" | out-null
    $nodeName = $Matches["node"]
    $nodes[$nodeName] = @{
        left = $Matches["left"];
        right = $Matches["right"];
    }

    if($nodeName.EndsWith("A")) {
        $startingKeys += $nodeName
    }
}

$startingKeys | % {
    $current = $nodes[$_]
    $target = ""
    $i = 0
    $steps = 0

    while(-not $target.EndsWith("Z")) {
        $steps++
        $target = if ($instruction[$i] -eq "L") { $current["left"] } else { $current["right"] }
        $current = $nodes[$target]
        $i++
        if ($i -eq $instruction.Length) {
            $i = 0
        }
    }
    $startingKeysSteps += $steps
}

Function Get-PrimeFactorsForNumber([int] $number) {
    $result = @()
    while( $number % 2 -eq 0 ) {
        $result += 2
        $number = $number / 2
    }

    for ($i = 3; $i -le [math]::Sqrt($number); $i = $i + 2) {
        while($number % $i -eq 0) {
            $result += $i
            $number = $number / $i
        }
    }

    if ($number -gt 2) {
        $result += $number
    }
    return $result
}

$primeFactors = @()
$startingKeysSteps | % {
    Get-PrimeFactorsForNumber($_) | % {
        $primeFactors += $_
    }
}

$total = 1
$primeFactors | Select -unique | % {
    $total = $total * $_
}

$total