import java.io.File

class Graph {
    private val nodes = mutableMapOf<String, List<String>>()
    
    fun addNode(name: String, links: List<String>) {
        nodes[name] = links
    }
    
    fun getGroup(name: String): List<String> {
        val group = mutableListOf<String>()
        val q = ArrayDeque<String>()
        q.add(name)
        while (true) {
            with(q.removeFirstOrNull() ?: break) {
                if (!group.contains(this)) {
                    group.add(this)
                    q.addAll(nodes[this]!!)
                }
            }
        }
        return group
    }
    
    fun countGroups(): Int {
        val checked = mutableListOf<String>()
        var count = 0
        
        for (node in nodes.keys) if (!checked.contains(node)) {
            checked.addAll(getGroup(node))
            count++
        }
        return count
    }
}

fun main() {
    val pipes = Graph()
    for (line in File("../__in/12.txt").readLines()) {
        val node = Regex("""(\d+)""").findAll(line).map { it.value }.toList()
        pipes.addNode(node[0], node.subList(1, node.size))
    }
    
    println("Part 1: ${pipes.getGroup("0").size}")
    println("Part 2: ${pipes.countGroups()}")
}