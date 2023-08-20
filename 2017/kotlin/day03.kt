import java.io.File
import kotlin.math.*

fun main() {
    val input = File("03.txt").readText().toInt()
    
    val a = with(ceil(sqrt(input.toDouble())).toInt()) { if (this % 2 != 0) this else this + 1 }
    // i hope math gods won't smite me but i couldn't help these polar coords similarities
    val heheRadius = (a - 1) / 2
    val heheAngle = abs((input - (a - 2) * (a - 2)) % (heheRadius * 2) - heheRadius)
    println("Part 1: ${heheRadius + heheAngle}")
    
    // ri-ight, let's set up the grid generator
    val grid = mutableMapOf( Pair(0, 0) to 1 )
    var direction = Pair(1, 0)
    
    var newNode = Pair(0, 0)
    var value: Int
    do {
        newNode += direction
        value = 0
        for (i in newNode.first - 1..newNode.first + 1)
            for (j in newNode.second - 1..newNode.second + 1) {
                value += grid[Pair(i, j)] ?: 0
            }
        grid[newNode] = value
        if (!grid.containsKey(newNode + turnLeft(direction))) direction = turnLeft(direction)
    } while (value <= input)
    println("Part 2: $value")
}