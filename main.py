import engine as en
from engine import start_engine
import tab as tb
from tab import start_tab
import threading as thrd

# start the engineto accses the model and camera
# en.start_engine()
# tb.start_tab()

t1 = thrd.Thread(target=start_engine)
t2 = thrd.Thread(target=start_tab)

t1.start()
t2.start()

# start_engine()