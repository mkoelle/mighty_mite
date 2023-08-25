<script lang="ts">
  import { Indicator, Badge } from "flowbite-svelte";
  export let ssid     = "Network SSID"
  export let security = "Security"
  export let channel = "Channel"
  export let strength = -50
  // export let Known    = false
  const strengthToColor = (s:number) => {
    // -30 dBm is Maximum signal strength
    if(s > -50){
      // up to -50 is excelent
      return "green"
    } else if (s > -60){
      // -50 to -60 is good
      return "indigo"
    } else if (s > -67){
      // -60 to -67  is minimum for streaming
      return "yellow"
    } else if (s > -70){
      // -67 to -70 is decent for simple things
      return "purple"
    } else if (s > -80){
      // -70 to -80 is minimum to make a connection
      return "blue"
    }
    return "red"
  }
</script>

<div class="flex items-center space-x-3">
  <div class="flex-1 min-w-0">
    <p class="text-sm font-semibold text-gray-900 truncate dark:text-white">
      {ssid}
    </p>
    <p class="text-sm text-gray-500 truncate dark:text-gray-400">Ch: {channel} Sec: {security}</p>
  </div>
  <Badge color="{strengthToColor(strength)}" rounded class="px-2.5 py-0.5">
    <Indicator color="{strengthToColor(strength)}" size="xs" class="mr-1" />{strength}
  </Badge>
</div>
