import java.io.File

fun main() {
    val input = File("../__in/19.txt").readLines()
    
    var pos = Pair(0, input[0].indexOfFirst { it != ' ' } ) // first is row index, second is column
    var dir = Pair(1, 0)            // we pretty much have regular (x, y) axes rotated 90° clockwise
    var tile: Char                  // so turnLeft / turnRight just happen to work without any changes
    var str = ""
    var step = 0
    
    do {
        pos += dir; step++
        tile = input[pos.first][pos.second]
        if (tile.isLetter()) str += tile
        else if (tile == '+') {
            with (pos + turnLeft(dir)) { dir = if (input[this.first][this.second] != ' ') turnLeft(dir) else turnRight(dir) }
        }
    } while (tile != ' ')
    
    println("Part 1: $str")
    println("Part 2: $step")
}