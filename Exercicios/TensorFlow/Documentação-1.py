import tensorflow as tf

no1 = tf.constant(3, dtype=tf.float32)

no2 = tf.constant(6.0)

sessao = tf.Session()

print no1, no2

print sessao.run([no1,no2])

no3 = tf.add(no1, no2)

print no3

