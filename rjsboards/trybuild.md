 title:  Here we go
 date:  20260511

### Steps to build `micropython`  zephyr for `seeed nrf52840`.

Assumes zephyr (sdk and west) have been installed:

 + `>~/zephyr-sdk-0.17.4/`   The zephyr SDK
 + `>~/work/nrfzephyr/`    The zephyr project directory
 + `>~/work/micropython/`  The current micropython repository

<details>
<summary>Script to set zephyr work environment `myzephyr.script`</summary>

``` bash
#!/bin/bash

_MYZEPHYR=${HOME}/work/nrfzephyr

dozephyr() {
    local myz
    if [ $# -eq 1 ]; then
	    myz=$1
    else
	    myz=$_MYZEPHYR
    fi
    source $myz/.venv/bin/activate
    source $myz/zephyr/zephyr-env.sh
}
```
</details>
Work flow to build for nrf52840

``` sh
>cd ~/work
>dozephyr     # from bash_alias

>west build -p always -b xiao_ble/nrf52840/sense micropython/ports/zephyr 2>&1 | tee build.upy_newx.2026051
>mkdir t4;mv build/zephyr/zephyr.uf2 t4
```


  >  Here is a block quote region
  >  What happens to this

