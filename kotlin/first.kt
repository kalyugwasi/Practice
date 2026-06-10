import java.util.*
fun calculate(ha:String,a:Int,b:Int):Int{
    if (ha == "add"){
        return a+b
    }
    return 0
}
fun main(){
    val scanner = Scanner(System.`in`)
    println("enter first value: ")
    var a = scanner.nextInt()
    println("enter second value: ")
    var b = scanner.nextInt()
    val ha = "add"
    println(calculate(ha,a,b))
}