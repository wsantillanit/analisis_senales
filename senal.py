import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 1. Definición del tiempo
# ----------------------------
fs = 1000                      # frecuencia de muestreo
t = np.linspace(0, 1, fs)      # 1 segundo

# ----------------------------
# 2. Generación de señales
# ----------------------------
f1 = 5
f2 = 10

senal1 = np.sin(2*np.pi*f1*t)
senal2 = np.sin(2*np.pi*f2*t)

senal_total = senal1 + senal2

# ----------------------------
# 3. Dominio del tiempo
# ----------------------------
plt.figure()
plt.plot(t, senal_total)
plt.title("Señal en el dominio del tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.show()

# ----------------------------
# 4. Transformada de Fourier
# ----------------------------
fft_signal = np.fft.fft(senal_total)
frecuencias = np.fft.fftfreq(len(t), 1/fs)

# ----------------------------
# 5. Dominio de la frecuencia
# ----------------------------
plt.figure()
plt.plot(frecuencias, np.abs(fft_signal))
plt.title("Espectro de frecuencia")
plt.xlabel("Frecuencia")
plt.ylabel("Magnitud")
plt.show()
