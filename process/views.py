from django.shortcuts import render, redirect
import psutil
''' აპლიკაცია იყენებს პსუტილის მოდულს.'''


def process_monitor(request):
    """ ფუნქცია ფრონტიდან, მიღებული რექსვესტის შემდეგ, ამოწმებს ოპერაციულ სისტემას და 
    ამის მიხედვით ადგენს, რომელი კონდიცია გაუშვას. """
    
    if psutil.LINUX:
        # ეს ნაწილი უნდა გააქტიურდეს თუ კომპიუტერის ოპერაციული სისტემა არის ლინუქსი.
        
        if request.method == 'POST':
            stop_process = request.POST.get('stop')
            resume_process = request.POST.get('resume')
            terminate_process = request.POST.get('terminate')
            # აქედან მოწმდება ფრონტიდან რომელ ღილაკს დაეჭირა. 
            # და ღილაკზე დაჭერის მიხედვით აქტიურდება, შესაბამისი ოპერაცია სერვისზე.
            
            try:    
                # შეაჩერე პროცესი.
                if stop_process:
                    stop1 = int(stop_process)
                    stop2 = psutil.Process(pid=stop1)
                    stop2.suspend()
                    return redirect('/')

                # განაახლე პროცესი.    
                if resume_process:
                    rezum1 = int(resume_process)
                    rezum2 = psutil.Process(pid=rezum1)
                    rezum2.resume()
                    return redirect('/')
            
                # გააუქმე პროცესი.
                if terminate_process:
                    terminate = int(terminate_process)
                    terminate2 = psutil.Process(pid=terminate)
                    terminate2.terminate()
                    return redirect('/')
                
            except psutil.NoSuchProcess:
                pass
        
        context = {'detail': psutil.process_iter(),
               #'serviz': func(),
               'cpu_percent': psutil.cpu_percent(),
               'memory_percent': psutil.virtual_memory(),}
        
        return render(request, 'process/processess.html', context)          
    
    # ვინდოუსი.
    else:
        stop_process = request.POST.get('stop')
        resume_process = request.POST.get('resume')
        terminate_process = request.POST.get('terminate')
        try:       
            # შეაჩერე პროცესი.
            if stop_process:
                stop1 = int(stop_process)
                stop2 = psutil.Process(pid=stop1)
                stop2.suspend()
                return redirect('/')
                
            # განაახლე პროცესი.
            if resume_process:
                rezum1 = int(resume_process)
                rezum2 = psutil.Process(pid=rezum1)
                rezum2.resume()
                return redirect('/')

            # გააუქმე პროცესი.    
            if terminate_process:
                terminate = int(terminate_process)
                terminate2 = psutil.Process(pid=terminate)
                terminate2.terminate()
                return redirect('/')
        
        except psutil.NoSuchProcess:
                pass

    context1 = {'detail': psutil.process_iter(),
               'service': psutil.win_service_iter(),
               'cpu_percent': psutil.cpu_percent(),
               'memory_percent': psutil.virtual_memory()}
        
    return render(request, 'process/processess.html', context1)

        