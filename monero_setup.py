import sys

cpu_cores = int(sys.argv[1])
gpu_count = int(sys.argv[2])

#Change file_path to where you installed xmr-stak
file_path = 'C:\\PlaceYouInstalledXmrStak\\xmr-stak-win64-2.5.2\\'

cpu_file_output = file_path + 'cpu.txt'
gpu_file_output = file_path + 'nvidia.txt'


def setup_cpu(cpu_cores):
    assert cpu_cores >= 0
    assert cpu_cores <= 16

    core_str = ''

    for i in range(0, cpu_cores):
        core_str += (
            '    { "low_power_mode" : false, "no_prefetch" : true, '
            '"asm" : "auto", "affine_to_cpu" : ' + str(2*i) + ' },' + '\n'
        )

    result = (
        '"cpu_threads_conf" :' + '\n' +
        '[' + '\n' +
        core_str + '\n' +
        '],' + '\n'
        )

    return result


def setup_gpu(gpu_count):
    assert gpu_count >= 0
    assert gpu_count <= 4

    gpu_str = ''

    for i in range(0, gpu_count):
        gpu_str += (
            '  { "index" : ' + str(i) + ',' + '\n'
            '    "threads" : 4, "blocks" : 224,' + '\n'
            '    "bfactor" : 6, "bsleep" :  25,' + '\n'
            '    "affine_to_cpu" : false, "sync_mode" : 3,' + '\n'
            '"mem_mode" : 1,' + '\n'
            '  },' + '\n'
            )

    result = (
        '"gpu_threads_conf" :' + '\n' +
        '[' + '\n' +
        gpu_str + '\n' +
        '],' + '\n'
        )

    return result


with open(cpu_file_output, 'w') as cpu_file:
    try:
        cpu_file.write(setup_cpu(cpu_cores))
        print('Successfully created ' + cpu_file_output)
    except Exception as e:
        print('Unable to write file: ' + cpu_file_output)
        raise e


with open(gpu_file_output, 'w') as gpu_file:
    try:
        gpu_file.write(setup_gpu(gpu_count))
        print('Successfully created ' + gpu_file_output)
    except Exception as e:
        print('Unable to write file: ' + gpu_file_output)
        raise e
