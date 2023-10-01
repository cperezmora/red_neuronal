# Redes Neuronales con TensorFlow y Keras
Este repositorio contiene ejemplos de implementación de redes neuronales usando TensorFlow y Keras. Se incluyen ejemplos de redes neuronales densamente conectadas, redes neuronales convolucionales y redes recurrentes.

## Uso
Para utilizar cualquiera de los modelos, primero instala las dependencias:

pip install tensorflow keras

Luego, ejecuta el script asociado para entrenar y evaluar el modelo correspondiente.

## Características
Redes Densamente Conectadas: Estas son las redes neuronales tradicionales donde cada neurona está conectada a todas las neuronas en la capa anterior y siguiente.

Redes Neuronales Convolucionales (CNN): Especialmente útiles para procesar imágenes y detectar patrones locales y jerarquías de patrones.

Redes Recurrentes (RNN): Adecuadas para secuencias de datos, como series temporales o secuencias de texto.

Optimización de rendimiento: Este código se beneficiará del uso de instrucciones específicas del CPU como AVX2 y FMA si están disponibles. Para habilitarlas, se debe compilar TensorFlow con los flags de compilador adecuados.

## Tips y solución de problemas
Si te encuentras con el error [SSL: CERTIFICATE_VERIFY_FAILED], es posible que necesites instalar certificados para Python. En sistemas macOS, se puede hacer corriendo el siguiente comando:

/Applications/Python\ 3.x/Install\ Certificates.command
El entrenamiento de las redes neuronales puede variar en tiempo por diversas razones como la cantidad de datos, la complejidad del modelo y la capacidad de cálculo disponible.

## Resultados y análisis

Resultados:
MLP Accuracy: 0.9754999876022339
CNN Accuracy: 0.9876999855041504
RNN Accuracy: 0.9818999767303467

MLP (Multi-Layer Perceptron) Accuracy: 0.9755
Descripción: Un perceptrón multicapa es una red neuronal densamente conectada. Su precisión es del 97.55%, lo que indica que, de cada 100 predicciones hechas por el modelo, aproximadamente 97.55 son correctas.
Análisis: Para muchas tareas, un 97.55% de precisión es bastante alto. Sin embargo, todo depende del contexto y de la complejidad del conjunto de datos. Por ejemplo, en reconocimiento de dígitos escritos a mano (como el dataset MNIST), este podría considerarse un buen rendimiento, pero no excepcional.

CNN (Convolutional Neural Network) Accuracy: 0.9877
Descripción: Las redes neuronales convolucionales son especialmente diseñadas para tratar datos con estructura de cuadrícula, como imágenes. La precisión de esta CNN es del 98.77%.
Análisis: Un 98.77% de precisión es excelente. Las CNNs suelen destacar en tareas relacionadas con imágenes debido a su capacidad para detectar características jerárquicas y patrones locales. Si estás trabajando con imágenes o datos con una estructura similar, este resultado indica que la CNN es muy efectiva para tu conjunto de datos.

RNN (Recurrent Neural Network) Accuracy: 0.9819
Descripción: Las redes neuronales recurrentes son ideales para secuencias de datos, como series temporales o texto. Esta RNN tiene una precisión del 98.19%.
Análisis: Un 98.19% es también un resultado muy bueno. Si estás trabajando con datos secuenciales, indica que tu RNN está capturando eficientemente las dependencias temporales o secuenciales en tus datos.

Conclusión General:
Todos los modelos muestran una precisión alta, siendo la CNN la que tiene el rendimiento más alto con un 98.77% de precisión. Si tu objetivo es seleccionar el modelo con el mejor rendimiento para una implementación posterior, la CNN sería la opción recomendada basándonos solo en precisión. Sin embargo, la elección del modelo también debería considerar otros factores como el tiempo de entrenamiento, la complejidad del modelo y el tipo específico de datos con los que estás trabajando.

## Licencia

Este proyecto está bajo la licencia MIT. Consulte el archivo `LICENSE` para obtener más detalles.

## MIT License

Copyright (c) [2023] [Carmen Pérez]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.