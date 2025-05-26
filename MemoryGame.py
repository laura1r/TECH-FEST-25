import flet as ft
from flet import *
import flet_audio as fta
import time
import random
 
def main(page: ft.Page):
     page.horizontal_alignment = "center"
     page.vertical_alignment = "center"
     page.bgcolor = "black"
     page.update()
     
     # 5 rows for the board
     row1 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[])
     row2 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[])
     row3 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[])
     row4 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[])
     row5 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[])
     
     rowlist = [row1, row2, row3, row4, row5]
     
     for i in range(1, 26):
        container = ft.Container(content=ft.Text(str(i), color="transparent"), data=i, margin=-2, padding=12,
                                   alignment=ft.alignment.top_left, bgcolor="white", width=65, height=65,
                                   border_radius=0, on_click=None)
          
        if 1 <= i <= 5: rowlist[0].controls.append(container)
        elif 6 <= i <= 10: rowlist[1].controls.append(container)
        elif 11 <= i <= 15: rowlist[2].controls.append(container)
        elif 16 <= i <= 20: rowlist[3].controls.append(container)
        elif 21 <= i <= 25: rowlist[4].controls.append(container)
          
        #Randomizer
        purplevalues = {random.randint(1, 25) for _ in range(11)}
        
        #Audios
        audio1 = fta.Audio(src="WinGameSound.mp3")
        page.overlay.append(audio1)

        audio2 = fta.Audio(src="EndGameSound.wav")
        page.overlay.append(audio2)
        
        def startGame(e):
               page.controls.remove(startrow)
               for row in rowlist:
                    page.add(row)
               
               #change containers colors
               for row in rowlist:
                    for container in row.controls:
                         if container.data in purplevalues:
                              container.bgcolor = "purple"
               page.update()
                              
               #change them back to white
               time.sleep(3)
               
               for row in rowlist:
                    for container in row.controls:
                         if container.data in purplevalues:
                              container.bgcolor = "white"
 
                    for row in rowlist:
                         for container in row.controls:
                              container.on_click = click  
               page.update()
          
        def click(e):
               container = e.control
               container.bgcolor = "purple"
               clickedpurple.add(container.data)
 
               if container.data in purplevalues:
                    text.value = ""
                    
               if container.data in purplevalues:
                    if clickedpurple == purplevalues:
                         for row in rowlist:
                              if row in page.controls:
                                   page.controls.remove(row)
                                   text.value = "Game Won"
                                   audio1.play()
                                   if titlerow in page.controls:
                                        page.controls.remove(titlerow)

               else: 
                    for row in rowlist:
                         if row in page.controls:
                              page.controls.remove(row)
                              text.value = "End Game"
                              audio2.play()
                              if titlerow in page.controls:
                                   page.controls.remove(titlerow)
               page.update()
    
     #track purple containers
     clickedpurple = set()
         
     #design
     text = Text(size=22, weight="bold", color="white")
     title = ft.Text("Memory Game", size=22, weight="bold", color="white")
     start = ft.Container(content=ft.ElevatedButton(
          on_click=startGame, content=ft.Text("Start", size=13, weight="bold", color="grey"),
          style=ft.ButtonStyle( shape={"": ft.RoundedRectangleBorder(radius=8)}, color={"": "white"}), height=45, width=255))
     
     #specific rows
     startrow = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[start])
     titlerow = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[title])
     
     page.add(titlerow,
              ft.Divider(height=20, color="transparent"),
              startrow, text)
ft.app(target=main, assets_dir="assets")