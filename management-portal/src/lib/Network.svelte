<script lang="ts">
  import { Indicator, Badge } from "flowbite-svelte";
</script>

<div class="flex items-center space-x-3">
  <div class="flex-1 min-w-0">
    <p class="text-sm font-semibold text-gray-900 truncate dark:text-white">
      Network Name
    </p>
    <p class="text-sm text-gray-500 truncate dark:text-gray-400">Security</p>
  </div>
  <Badge color="green" rounded class="px-2.5 py-0.5">
    <Indicator color="green" size="xs" class="mr-1" />-50
  </Badge>
</div>
