#Trabajo final de aprendizaje de maquinas.
Abel Molina Sanchez
Julio Jose Horta Vazquez

#Descripcion del problema:

Se quiere analizar las estadisticas de la Major League Beisball (MLB) para sacar datos interesantes sobre el hall de la fama de esta liga. Ademas se desea construir un modelo para predecir que jugadores que entran en el periodo de los ultimos 10 años van a ser seleccionados. Dado este modelo se desea observar que jugadores de la epoca de los esteriodes que se fueron sancionados tenian numeros de HOF. Por ultimo se desea ver si algunos jugadores de las ligas negras americanas que no fueron seleccionados para el HOF podrian haberse elegido por sus numeros.

#Busqueda de los datos

Para buscar los datos y estadisticas tuvimos que referirnos a la pagina web [BeisballReference](https://www.baseball-reference.com/). Aqui se hace un seguimiento exhaustivo de las estadisticas de cada jugador que haya competido en la MLB.

#Scrapper

Una vez identificados los datos necesitabamos una manera de extraerlos de forma automatizada de la pagina. La solucion llego con BeautifulSoup, libreria de python que nos permitio extraer la informacion completa de cada jugador de manera estructurada. Esto se puede ver en la carpeta del proyecto Scraper. Una vez creado el json general, se crearon varios json para guardar estadisticas mas personalizadas como es el caso de solo pitchers con estadisticas de picheo o bateadores con estadisticas de bateo y fildeo. Esto lo podemos emcontrar en la carpeta Data.

#Problema 1: Modelo predictor de HOF
NOTA: EL trabajo fue similar en ambos modelos (bateadores y pitchers). Explicaremos ambos procesos de manera simultnea haciendo las distinciones cuando se requiera. 
Lo primero fue cargar los datos utilizando la libreria pandas de python. Una vez estos estuvieron cargados, se empezo a hacer preguntas al dataset para ver la forma de estos. Se remplazo el valor "retirement_age" por la moda del conjunto en caso de que no se conociera el valor ya q no queriamos perder esos datos. con algunas estadisticas no se hizo esto y simplemente se obviaron mientras que para algunos jugadores del dataset se tomo la decision de desecharlos. Se utilizaron varios filtros para eliminar datos jugadores que no cumplieran con ciertos standares como que el WAR_pt> 15 o que los juagdores hubieran jugado cierta cantidad de juegos o años.
Tambien se quitaron los que aun estan en activo ya q estos no pueden entrar todavia.

Lo siguiente fue muestrear graficamente los valores en separando por colores a los que entraron al HOF y a los que no para tener idea de que aspecto espacial tenian los datos. En el caso de los bateadores las diferencias fueron practicamente inexistentes de cada característica entre los que entraron y los que no, en los pitchers aunq hubo mas diferencias aun asi no eran muy grandes.

Seguidamente revisamos la correlacion entre las variables y notamos que la mayor correlacion entre variables estaba en las variables avanzdas, lo cual es coherente ya que estas usan estadisticas simples para calcularse.Revisando esto y la importancia que tenian las caracteristicas en los modelos decidicimos quedarnos con un reducido subconjunto de estas.

El paso antes de empezar a correr los modelos fue separar los datos en conjunto de entrenamiento, testeo y validacion.

#Corriendo los modelos

Lo primero que hicimos fue calcular la prediccion negativa cuyos valores dieron Accuracy: 0.8758 y AUC: 0.5000 ambas son metricas que revisan la presicion del modelo. Despues corrimos los diferentes modelos y los comparamos, ademas de ver las graficas donde se muestra el bias y variance, para revisar si pueden ser usados o no los modelos. Aca en el caso de los bateadores se tuvo algunos modelos con buen perfomance y otros no, en el caso de los pitchers la mayoria fueron malos perfomance dadas las graficas.

Luego probamosreducir dimensiones para ver si se lograba afectar al modelo positivamente. Utilizamos Linear-Discriminant-Analysis para esto. AL volver a correr los nuevos modelos se volvio a comparar que tan buenos eran los resultados. Nuevamente se obtuvieron modelos buenos y otros malos  pero mejores que los anteriores. en su mayoria.






