le = int(input("How many process you have :"))
p_at = [0]*le
p_name = ["None"]*le
p_bt = [0]*le
p_wt=[0]*le
tt = [0]*le
sub_ap_wt = 0
sub_att = 0
for i in range (le):
    p_name[i] = str(input("Enter process name :"))
    p_at[i] = int(input("Enter Arrival time :"))
    p_bt[i] = int(input("Enter burst time :"))
    print()


for i in range (0, le):
    for j in range (i+1, le):
        if (p_at[i]>p_at[j]):
            temp = p_at[i]
            p_at[i] = p_at[j]
            p_at[j] = temp

            temp = p_name[i]
            p_name[i] = p_name[j]
            p_name[j] = temp

            temp = p_bt[i]
            p_bt[i] = p_bt[j]
            p_bt[j] = temp

g_s = [0]*le
g_e = [0]*le
temp = 0
for i in range (0,le):
    if p_at[i]<=0:
        g_s[i]=0
    else:
        if i==0:
            g_s[i]=p_at[i]
            temp = g_s[i]
        else:
            g_s[i] = temp + p_bt[i-1]
            temp = g_s[i]

for i in range (0,le):
    g_e[i] = g_s[i] + p_bt[i]

print(g_s)
print(g_e)

for i in range (le):
    p_wt[i] = g_s[i] - p_at[i]
    tt[i] = p_wt[i] + p_bt[i]

print(p_wt)
print(tt)

for i in range (le):
    sub_ap_wt += p_wt[i] 
    sub_att += tt[i]
ap_wt = sub_ap_wt/le
att = sub_att/le

print()
print()
print("process Name \t Arrival Time \t Burst Time \t Waiting Time \t Turnaround Time")
for i in range (le):
    print(p_name[i],"\t\t",p_at[i],"\t\t",p_bt[i],"\t\t",p_wt[i],"\t\t",tt[i])