# Ground Truth

For this project we will be using a **calculated ring radius** as our ground truth. This calculated ring radius is obtained by using the following function based on the standard formula to calculate the angle of the [Cherekov Radiation Cone](https://indico.cern.ch/event/1156680/contributions/4857473/attachments/2471565/4240363/PID_Lecture_HighRR_Germany_June_2022.pdf):

`def calc_ring_radius(m,p):`

`"""`

`Returns the expected ring radius [m]`

`m : mass of the particle in MeV/c^2`

`p : track momentum in MeV/c`

`"""`

`F_M = 17.0 # Focal length [m]`

`N = 1 + 62.8e-6 # Neon refractive index`

`r = F_M*N*p*np.sqrt(1 - (m**2 + p**2)/(N**2*p**2))/np.sqrt(m**2 + p**2)`

`return r`

Moving forward we will refer to this calculated value as the **'Theoretical Ring Radius'**
