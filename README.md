# 16 key hackpad with OLED
This is my 16-key hackpad which has 16 keys and an oled screen. I made it so I can use all 16 keys for different shortcuts and stuff, because I'm not bothered to move  my hand an extra 2mm every 10 hours. This is my CAD, I looked at the kicad pcb and measured with the ruler to find the measurements to place the oled and keys in the correct places. The CADing was pretty easy overall.

<img width="674" height="385" alt="Screenshot 2026-03-22 at 6 55 59 pm" src="https://github.com/user-attachments/assets/44034d05-c7f0-4596-9489-7d23239a327d" />
<img width="718" height="533" alt="Screenshot 2026-03-22 at 6 55 48 pm" src="https://github.com/user-attachments/assets/9a6e8091-df33-469d-936e-809327c6a7f0" />
<img width="582" height="455" alt="Screenshot 2026-03-22 at 6 55 44 pm" src="https://github.com/user-attachments/assets/2ef83306-f6f2-4030-80d5-89ea78c5ac62" />
<img width="799" height="401" alt="Screenshot 2026-03-22 at 6 55 26 pm" src="https://github.com/user-attachments/assets/ad354cd6-f794-4fc2-bbe0-36f3b049bf5d" />

This is my PCB design, after creating the schematic, I imported it into the pcb editor and arranged the parts, which was pretty easy. But then I had to do the wiring, I started from the top and went down but it was extremely annoying and mind-numbing, finally, after a while, I managed to complete it. I have so many vias... :( I also had a bit of trouble fitting it into the 100 by 100 millimetre pcb size limit, but I barely made it.

<img width="591" height="582" alt="Screenshot 2026-03-22 at 7 51 20 pm" src="https://github.com/user-attachments/assets/414d0d72-f4b6-4e21-a585-9e1f72605d29" />

This is my schematic, I started by creating the 4 by 4 matrix for the buttons, then I connected it to the rp2040. Next, I added the oled and connected that to the rp2040. The hardest part was creating the matrix which took me a while and a lot of reddit searching, but after that, it got a lot simpler.

<img width="802" height="469" alt="Screenshot 2026-03-22 at 8 11 09 pm" src="https://github.com/user-attachments/assets/63e248ad-4e9b-4bea-9332-c10e1781ee5f" />

