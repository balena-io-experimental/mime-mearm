# Resin.io + Picon Zero + Mime MeArm

This is a project to get you started with the [4tronix Picon Zero][piconzero] and the awesome [Mime MeArm][mearm] on resin.io.

![Alt text](image.jpg?raw=true "Mime MeArm")
![Alt text](interface.png?raw=true "User interface")

## Usage

1. Provision a device in your application following this [Getting Started Guide][resin-get-started].
2. Clone this repository locally and add the `resin git remote` to the repo.
3. Run `git push resin master` and wait for the code to be deployed.
4. Set some `Application config variables` (only needed if you want to use a picam for visual feedback)
    * `RESIN_HOST_CONFIG_gpu_mem=128`
    * `RESIN_HOST_CONFIG_start_x=1`
5. In your browser navigate to `<IP-ADDRESS>:5000`

[piconzero]:http://4tronix.co.uk/piconzero/
[mearm]:http://4tronix.co.uk/piconzero/
[resin-get-started]:https://docs.resin.io/raspberrypi3/python/getting-started/
