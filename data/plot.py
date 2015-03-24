from pylab import *

case = 4

if  case == 1: #  cache size 512k
    
    Tlru1 = array([24142078, 22622696, 16668372, 24002821, 38620550]) / 1e6
    Tlru2 = array([25117047, 20180217, 23708645, 20302015, 21014371]) / 1e6
    
    Tfifo1 = array([16270058, 18006636, 39432443, 16073421, 16508937]) / 1e6
    Tfifo2 = array([20392172, 24345019, 17929862, 17426216, 18767222]) / 1e6

    Tran1 = array([20750768, 27767790, 22320682, 19495321, 21360395]) / 1e6
    Tran2 = array([21476919, 19854635, 21848175, 20770845, 19912484]) / 1e6

    Tno1 = array([38864197, 26762765, 27486469, 33065761, 35756185]) / 1e6
    Tno2 = array([28779805, 27907490, 29268581, 32579494, 29494877]) / 1e6

    Hlru1 = array([49, 56, 56, 56, 56])
    Hlru2 = array([36, 38, 38, 38, 38])
    
    Hfifo1 = array([47, 52, 52, 52, 52])
    Hfifo2 = array([41, 43, 43, 43, 43]) 

    Hran1 = array([39, 51, 57, 52, 46])
    Hran2 = array([34, 31, 34, 37, 40])
    
    x = arange(1, 6)
    T1 = [Tlru1,  Tfifo1, Tran1, Tno1]
    T2 = [Tlru2,  Tfifo2, Tran2, Tno2]
    H1 = [Hlru1, Hfifo1, Hran1]
    H2 = [Hlru2, Hfifo2, Hran2]
    
    # plot the time 
    fig = figure(figsize=(10,4.5))
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    lab1 = ['lru', 'FIFO', 'Random', 'no cache']
    for i in range(4):
        ax.plot(x, T1[i], '-o', label = lab1[i] )
        ax2.plot(x, T2[i], '-o', label = lab1[i] )
    ax.set_xlabel(" the k th run")
    ax.set_xticks(range(1,6))
    ax.set_ylabel(r"time : second")
    ax.set_title('(a) repeated workload')
    ax.set_ylim([15, 50])
    ax.grid()
    ax.legend(loc='best')
    ax2.set_xlabel(" the k th run")
    ax2.set_xticks(range(1,6))
    ax2.set_ylabel(r"time : second")
    ax2.set_title('(b) random workload')
    ax2.set_ylim([15, 50])
    ax2.grid()
    tight_layout()
    ax2.legend(loc='best')
    show()

    # plot miss rate
    fig = figure(figsize=(10,4.5))
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    lab1 = ['lru', 'FIFO', 'Random', 'no cache']
    for i in range(3):
        ax.plot(x, H1[i] / double(110), '-o', label = lab1[i] )
        ax2.plot(x, H2[i] / double(110), '-o', label = lab1[i] )
    ax.set_xlabel(" the k th run")
    ax.set_xticks(range(1,6))
    ax.set_ylabel("Hit rate")
    ax.set_title('(a) repeated workload')
    ax.set_ylim([0.3, 0.7])
    ax.grid()
    ax.legend(loc='best')
    ax2.set_xlabel(" the k th run")
    ax2.set_xticks(range(1,6))
    ax2.set_ylabel("Hit rate")
    ax2.set_title('(b) random workload')
    #ax2.set_ylim([15, 50])
    ax2.grid()
    tight_layout()
    ax2.legend(loc='best')
    show()


    
if case == 2: # cache 256k

    Tlru1 = array([26710951, 31449619, 34317350, 33886474, 31371425]) / 1e6
    Tlru2 = array([36777998, 25900562, 25980285, 25845083, 25094305]) / 1e6
    
    Tfifo1 = array([29118578, 32270436, 34999665, 27073794, 28982076]) / 1e6
    Tfifo2 = array([29290473, 27183260, 30463444, 31124121, 55086133]) / 1e6

    Tran1 = array([33432324, 24299908, 25774833, 23677381, 29190353]) / 1e6
    Tran2 = array([25536008, 25776198, 26321355, 23227919, 28174831]) / 1e6

    Tno1 = array([38864197, 26762765, 27486469, 33065761, 35756185]) / 1e6
    Tno2 = array([28779805, 27907490, 29268581, 32579494, 29494877]) / 1e6

    Hlru1 = array([9, 10, 10, 10, 10])
    Hlru2 = array([16, 17, 17, 17, 17])
    
    Hfifo1 = array([9, 10, 10, 10, 10])
    Hfifo2 = array([17, 17, 17, 17, 17]) 

    Hran1 = array([23, 26, 26, 29, 21])
    Hran2 = array([21, 21, 24, 27, 21])
    
    x = arange(1, 6)
    T1 = [Tlru1,  Tfifo1, Tran1, Tno1]
    T2 = [Tlru2,  Tfifo2, Tran2, Tno2]
    H1 = [Hlru1, Hfifo1, Hran1]
    H2 = [Hlru2, Hfifo2, Hran2]
    
    # plot the time 
    fig = figure(figsize=(10,4.5))
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    lab1 = ['lru', 'FIFO', 'Random', 'no cache']
    for i in range(4):
        ax.plot(x, T1[i], '-o', label = lab1[i] )
        ax2.plot(x, T2[i], '-o', label = lab1[i] )
    ax.set_xlabel(" the k th run")
    ax.set_xticks(range(1,6))
    ax.set_ylabel(r"time : second")
    ax.set_title('(a) repeated workload')
    ax.set_ylim([20, 50])
    ax.grid()
    ax.legend(loc='best')
    ax2.set_xlabel(" the k th run")
    ax2.set_xticks(range(1,6))
    ax2.set_ylabel(r"time : second")
    ax2.set_title('(b) random workload')
    ax2.set_ylim([20, 60])
    ax2.grid()
    tight_layout()
    ax2.legend(loc='best')
    show()

    # plot miss rate
    fig = figure(figsize=(10,4.5))
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    lab1 = ['lru', 'FIFO', 'Random', 'no cache']
    for i in range(3):
        ax.plot(x, H1[i] / double(110), '-o', label = lab1[i] )
        ax2.plot(x, H2[i] / double(110), '-o', label = lab1[i] )
    ax.set_xlabel(" the k th run")
    ax.set_xticks(range(1,6))
    ax.set_ylabel("Hit rate")
    ax.set_title('(a) repeated workload')
    #ax.set_ylim([0.3, 0.7])
    ax.grid()
    ax.legend(loc='best')
    ax2.set_xlabel(" the k th run")
    ax2.set_xticks(range(1,6))
    ax2.set_ylabel("Hit rate")
    ax2.set_title('(b) random workload')
    #ax2.set_ylim([15, 50])
    ax2.grid()
    tight_layout()
    ax2.legend(loc='best')
    show()

if case == 3: # cache size 1M

    Tlru1 = array([11045402, 12209758, 9371645, 8868806, 12377946]) / 1e6
    Tlru2 = array([11248460, 10456043, 10219191, 12587708, 10673209]) / 1e6
    
    Tfifo1 = array([12598023, 12846641, 10415344, 10975996, 11500970]) / 1e6
    Tfifo2 = array([11997001, 11873173, 13689131, 12730854, 43549401]) / 1e6

    Tran1 = array([15558349, 17657252, 11965531, 9262124, 11392864]) / 1e6
    Tran2 = array([11854422, 9705864, 11215788, 13784642, 11106649]) / 1e6

    Tno1 = array([38864197, 26762765, 27486469, 33065761, 35756185]) / 1e6
    Tno2 = array([28779805, 27907490, 29268581, 32579494, 29494877]) / 1e6

    Hlru1 = array([77, 89, 89, 89, 89])
    Hlru2 = array([68, 74, 74, 74, 74])
    
    Hfifo1 = array([72, 84, 84, 84, 84])
    Hfifo2 = array([71, 74, 74, 74, 74])

    Hran1 = array([69, 74, 79, 89, 84])
    Hran2 = array([65, 74, 74, 69, 78])
    
    x = arange(1, 6)
    T1 = [Tlru1,  Tfifo1, Tran1, Tno1]
    T2 = [Tlru2,  Tfifo2, Tran2, Tno2]
    H1 = [Hlru1, Hfifo1, Hran1]
    H2 = [Hlru2, Hfifo2, Hran2]
    
    # plot the time 
    fig = figure(figsize=(10,4.5))
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    lab1 = ['lru', 'FIFO', 'Random', 'no cache']
    for i in range(4):
        ax.plot(x, T1[i], '-o', label = lab1[i] )
        ax2.plot(x, T2[i], '-o', label = lab1[i] )
    ax.set_xlabel(" the k th run")
    ax.set_xticks(range(1,6))
    ax.set_ylabel(r"time : second")
    ax.set_title('(a) repeated workload')
    #ax.set_ylim([20, 50])
    ax.grid()
    ax.legend(loc='best')
    ax2.set_xlabel(" the k th run")
    ax2.set_xticks(range(1,6))
    ax2.set_ylabel(r"time : second")
    ax2.set_title('(b) random workload')
    #ax2.set_ylim([20, 60])
    ax2.grid()
    tight_layout()
    ax2.legend(loc='best')
    show()

    # plot miss rate
    fig = figure(figsize=(10,4.5))
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    lab1 = ['lru', 'FIFO', 'Random', 'no cache']
    for i in range(3):
        ax.plot(x, H1[i] / double(110), '-o', label = lab1[i] )
        ax2.plot(x, H2[i] / double(110), '-o', label = lab1[i] )
    ax.set_xlabel(" the k th run")
    ax.set_xticks(range(1,6))
    ax.set_ylabel("Hit rate")
    ax.set_title('(a) repeated workload')
    #ax.set_ylim([0.3, 0.7])
    ax.grid()
    ax.legend(loc='best')
    ax2.set_xlabel(" the k th run")
    ax2.set_xticks(range(1,6))
    ax2.set_ylabel("Hit rate")
    ax2.set_title('(b) random workload')
    #ax2.set_ylim([15, 50])
    ax2.grid()
    tight_layout()
    ax2.legend(loc='best')
    show()

if case == 4:
    Hlru1 = array([91, 110, 110, 110, 110])
    x = arange(1, 6)
    # plot miss rate
    fig = figure(figsize=(6,4))
    ax = fig.add_subplot(111)
    lab1 = ['lru', 'FIFO', 'Random', 'no cache']
    ax.plot(x, Hlru1 / double(110), 'r-.o', lw = 2, label = lab1[0] )
    ax.plot(x, Hlru1 / double(110), 'y--o', lw =2, label = lab1[1] )
    ax.set_xlabel(" the k th run")
    ax.set_xticks(range(1,6))
    ax.set_ylabel("Hit rate")
    #ax.set_title('(a) repeated workload')
    ax.set_ylim([0.8, 1.1])
    ax.grid()
    ax.legend(loc='best')
    tight_layout()
    ax2.legend(loc='best')
    show()

     
