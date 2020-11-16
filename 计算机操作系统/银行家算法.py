class Process:
    def __init__(self, index: int, max_require: dict):
        self.sequence: list = []
        self.index: int = index
        self.max_require: dict = max_require
        self.allowed_resource: dict = {i: 0 for i in max_require.keys()}
        self.need_resource: dict = {i: self.max_require[i] - self.allowed_resource[i] for i in max_require.keys()}
        self.condition: bool = False

    def __call__(self):
        self.allowed_resource: dict = {i: 0 for i in self.max_require.keys()}
        self.need_resource: dict = self.max_require.copy()

    def _apply_resource(self, apply_inf: dict) -> None:
        for resource_name, resource_number in apply_inf.items():
            self.allowed_resource[resource_name] = min(self.max_require[resource_name],
                                                       self.allowed_resource[resource_name] + resource_number)
            self.need_resource[resource_name] = max(0, self.max_require[resource_name] - self.allowed_resource[
                resource_name])
        if not any(self.need_resource.values()):
            self.condition = True

    def _check_finished(self) -> bool:
        for resource_name, resource_number in self.max_require.items():
            if self.allowed_resource[resource_name] != resource_number:
                return False
        return True

    def _display_information(self):
        print(
            f'{self.index}\t\t\t{"  ".join([str(i) for i in self.max_require.values()])}\t\t\t\t'
            f'{"  ".join([str(i) for i in self.allowed_resource.values()])}\t\t\t\t{"  ".join([str(i) for i in self.need_resource.values()])}\t\t\t\t{self.condition}')


class ResourceControlCenter:
    def __init__(self, attainable_resource: dict):
        self.attainable_resource: dict = attainable_resource
        self.max_resource: dict = attainable_resource.copy()
        self.resource_name_list: list = list(attainable_resource.keys())

    def __call__(self):
        self.attainable_resource = self.max_resource.copy()

    def _take_back_or_allocate_resource(self, resource_dict: dict, flag: bool = False):
        if flag:
            for i in self.resource_name_list:
                self.attainable_resource[i] += resource_dict[i]
        else:
            for i in self.resource_name_list:
                self.attainable_resource[i] -= resource_dict[i]


class Banker:

    def allocate_resource(self):
        continue_flag: bool = True
        while continue_flag:
            p_index = eval(input('Input the number of process that you want to allocate resource:'))
            process: Process = self.works_dict.get(p_index)
            if process and not process.condition:
                allocate_dict: dict = {name: number for name, number in zip(self.rcc.resource_name_list,
                                                                            [int(i) for i in input('Input the number of resource:').split(' ')])}
                take_back_resource: dict = process.allowed_resource.copy()
                if not all([allocate_dict[i]<=self.rcc.attainable_resource[i] for i in self.rcc.resource_name_list]):
                    print('oversubscribe! Refuse allocate resource!')
                    continue
                process._apply_resource(allocate_dict)
                if process.condition:
                    self.rcc._take_back_or_allocate_resource(take_back_resource, flag=True)
                else:
                    self.rcc._take_back_or_allocate_resource(allocate_dict)
                self._check_safe()
            else:
                print('--->Process not exist or have finished.<---')
            self.work_list = [i for i in self.work_list if not i.condition]
            continue_flag = True if input('Do you want continue?(y/n)') == 'y' else False

    def _distribute_resource(self) -> None:
        attainable_resource: dict = {}
        resource_num: int = int(input('Please input the number of resource categories:'))
        for i in range(resource_num):
            p_name: str = input(f'The name of source {i}: ')
            p_resource: int = int(input('The number of source: '))
            attainable_resource[p_name] = p_resource
        self.rcc: ResourceControlCenter = ResourceControlCenter(attainable_resource=attainable_resource)



    def _initial_process(self) -> bool:

        self.works_number: int = int(input('Please input the number of works:'))
        self.works_dict: dict = {}
        print(
            f'Please input the max resource number that each process required(it must be a {self.works_number}x{len(self.rcc.resource_name_list)} matrix.):')
        for index in range(self.works_number):
            initial_list: list = [int(i) for i in input(':').split(' ')]
            self.works_dict[index] = Process(index=index, max_require={i: j for i, j in zip(self.rcc.resource_name_list, initial_list)})

        self.work_list = [i for i in self.works_dict.values()]

        overflow: bool = False
        print(
            f'Please input the allowed resource number that each process required(it must be a {self.works_number}x{len(self.rcc.resource_name_list)} matrix.):')
        for i in range(self.works_number):
            distribute_list = [int(i) for i in input(':').split(' ')]
            dis_dic = {i: j for i, j in zip(self.rcc.resource_name_list, distribute_list)}
            self.works_dict[i]._apply_resource(dis_dic)
        self.work_list = [i for i in self.work_list if not i.condition]
        return overflow

    def __init__(self):
        self._distribute_resource()
        self._initial_process()
        self._display()
        while not self._check_safe():
            re_flag = input(f'Do you want to reallocate resources?(y/n)')
            if re_flag == 'y':
                self._initial_process()
            else:
                print(f'--->Exit process<---')
                return
        self._display()

    def _display(self):
        print(f'\nEach resource available condition:')
        [print(f'--->The resource:{i}, which residue resource number:{j}') for i, j in
         self.rcc.attainable_resource.items()]
        print(f'\nIndex\t\tMax\t\t\t\tAllocation\t\t\t\tNeed\t\t\t\tstatus')
        for i in range(self.works_number):
            self.works_dict[i]._display_information()

    def _check_safe(self) -> bool:
        safe_sequence = []
        print('--->Conduct safety checks<---')

        def deep_search(work_list: list, residue_resource: dict, sol: list):
            if not safe_sequence:
                if not work_list:
                    safe_sequence.append(sol)
                for index, process in enumerate(work_list):
                    distribute_resource: list = [residue_resource[resource] - process.need_resource[resource] for
                                                 resource in self.rcc.resource_name_list]
                    if all([i >= 0 for i in distribute_resource]):
                        [residue_resource.update(
                            {resource: residue_resource[resource] + process.allowed_resource[resource]}) for resource in
                            self.rcc.resource_name_list]
                        deep_search(work_list=work_list[:index] + work_list[index + 1:],
                                    residue_resource=residue_resource, sol=sol + [process.index])

        deep_search(work_list=self.work_list[:], residue_resource=self.rcc.attainable_resource.copy(), sol=[])
        if safe_sequence:
            print('This system is secure!This secure execute sequence is:')
            [print(safe_sequence[0][i], end=' -> ') if i != len(safe_sequence[0]) - 1 else print(_) for i, _ in
             enumerate(safe_sequence[0])]
            return True
        else:
            print('This system is not secure! Take back all resource!')
            [i() for i in self.work_list]
            self.rcc()
            return False


res = []

x = Banker()
x.allocate_resource()
