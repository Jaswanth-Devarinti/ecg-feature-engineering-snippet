# %% Plotting
print("Do you want to plot R peak?")
choose_three = input("Proceed ([y]/n)?")
if choose_three == 'y':
     plt.plot(time, ml)
     plt.plot(peak,ml[peak], 'rv')
     for i, type in enumerate(type_plot):
         x = peak[i]
         y = ml[peak][i]
         plt.text(x, y+0.3, type, fontsize=9)
     plt.xlim(0, 10000)
     print("Done.")
     plt.show()
 else:
     if choose_three == 'n':
         print("Not Plotting, Done.")
     else:
         print("please input y or n")
         raise NameError