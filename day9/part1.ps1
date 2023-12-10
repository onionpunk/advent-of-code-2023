$file = Get-content "./input.txt"

Function Predict-NextNumber([int[]]$numbers) {
    $toAdd = 0
    $history = @()
    for($i=0; ($i+1) -lt $numbers.Length; $i++) {
        $history += $numbers[$i+1] - $numbers[$i]
    }

    if (($history | Get-Unique).Length -gt 1) {
        $toAdd = Predict-NextNumber($history)
    } else {
        $toAdd = $history[0]
    }
    $result = $numbers[$numbers.Length-1] + $toAdd
    $numbers += $result
    return $result
}

$total = 0;
$file | % {
    $line = $_
    $numbers = $line -split " "
    [array]::Reverse($numbers)
    $total += Predict-NextNumber($numbers)
}

$total