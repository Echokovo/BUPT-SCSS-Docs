ifneq ($(KERNELRELEASE),)
	obj-m := kthread.o
else
	KERNELDIR ?= /usr/src/kernels/4.19.90-2003.4.0.0036.oe1.x86_64
	PWD := $(shell pwd)
default:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules
endif
.PHONY:clean
clean:
	-rm *.mod.c *.o *.order *.symvers *.ko
