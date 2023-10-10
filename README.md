    ## == варианты загрузки драйвера==
    #### 1 вариант три вида загрузки страницы normal по умолчанию, none - ничего не ждет , eager загружает только DOM- дерево
    ### chrom_options.page_load_strategy = 'normal'
    
    #### с установленным размером
    ### chrom_options.add_argument("--window-size=1500, 900")
    #### максимальный размер
    ### chrom_options.add_argument("--start-maximized")
    #### 2 вариант безголовый режим без открытия браузера полезен в прогоне в CI CD
    #### chrom_options.add_argument("--headless")
    ##### 3 вариант зайти в режиме инкогнито
    ### chrom_options.add_argument("--incognito")
    #### ИГНОР сертификатов
    #### chrom_options.add_argument("--ignor-certificate-errors")
    
