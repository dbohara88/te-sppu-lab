package com.mandanatech.spark
import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.log4j._
object FriendsByAge {
def parsLine(line:String)={
val fields = line.split(",")
val name = fields(1).toString
val age = fields(2).toInt
(name,age)
}
def main(args: Array[String]): Unit = {
Logger.getLogger("org").setLevel((Level.ERROR))
val sc = new SparkContext("local[*]","FriendByAge")
val lines = sc.textFile("fakefriends.csv")
val rdd = lines.map(parsLine)
val rddCount = rdd.mapValues(x => (x,1))
val totalsByName = rddCount.reduceByKey((x,y) => (x._1+y._1,x._2+y._2))
val avarageAgeByName = totalsByName.mapValues(x => x._1/x._2)
val results = avarageAgeByName.collect()
results.sorted.foreach(println)
}
}