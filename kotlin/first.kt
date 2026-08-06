import java.util.*    
// fun main(){
//     var animal = "horse"
//     when(animal){
//         "horse" -> println("Animal is Horse")
//         "dog" -> println("Animal is dog")
//         "cat" -> println("Animal is cat")
//         else -> println("unknown animal")
//     }
// }
// fun main(){
//     var scan = Scanner(System.`in`)
//     println("Enter the percentage you got")
//     var percentage = scan.nextInt()
//     when(percentage){
//         in 90..100 -> println("He is a fucking topper")
//         in 80..90 -> println("was just about to be a topper")
//         in 50..80 -> println("you are an average dude")
//         in 35..50 -> println("god save you dude")
//         else -> println("dont come back again you failure")
//     }
// }
// fun main(){
//     var number: Int = 2689
//     var index: Int = 1
//     while(index<=10){
//         println("$number * $index = ${number*index}")
//         index++
//     }
// }
// fun main(){
//     var count = 0
//     for (i in 1..10 step 2){
//         println("hello $i")
//     }
//     for (i in 10 downTo 1 step 2){
//         println(i)
//     }
// }
//fun main(){
//    var fn: (Double,Double)->Double = ::addition
//    println(fn(1.0,4.0));
//    var fni: (Int,Int)-> Int = ::addition
//    println(fni(1,2));
//}

//fun addition(a: Int, b:Int): Int{
//    return a+b
//}

//fun addition(a:Double,b:Double): Double{
//    return a+b
//}
//fun main(){
//    var arr = arrayOf("one","two","three")
//    var arr1 = arrayOf(1,2,3)
//    var arr2 = arrayOf<Int>(3,4,5)
//    for ((i,e) in arr.withIndex()) println("$i - $e")
//    println(arr[0])
//    println(arr.get(2))
//    arr.set(0,"Hello")
//    println(arr[0])
//    println(arr.size)
//    for ((i,e) in arr.withIndex()) println("$i - $e")
//}
fun main(){
    val mustang = Car(name:"mustang",type:"petrol",kmRan: 100)
    val bettle = Car(name: "bettle",type:"diesel",kmRan:200)
    println(mustang.name)
    println(mustang.type)
    println(bettle.name)
    println(bettle.type)

    mustang.driveCar()

}   

class Car(val name: String, val type:String, var kmRan: Int){
    fn driveCar(){
        println("dirving car")
    }
    fn applyBreakes(){
        println("Car jjust applied brakes")
    }
}