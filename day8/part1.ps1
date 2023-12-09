$file = Get-content "./input.txt"

$instruction = $file[0]

$nodes = @{}

2..$file.Length | % {
    $line = $file[$_]
    $line -match "(?<node>.+) = \((?<left>.+), (?<right>.+)\)" | out-null
    $nodes[$Matches["node"]] = @{
        left = $Matches["left"];
        right = $Matches["right"];
    }
}

$current = $nodes["AAA"]
$target = ""
$i = 0
$steps = 0

while($target -ne "ZZZ") {
    $steps++
    $target = if ($instruction[$i] -eq "L") { $current["left"] } else { $current["right"] }
    $current = $nodes[$target]
    $i++
    if ($i -eq $instruction.Length) {
        $i = 0
    }
}
$steps