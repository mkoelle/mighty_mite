<script>
  import { Meta, Template, Story } from '@storybook/addon-svelte-csf';
  import Network from './Network.svelte';
  let defaults = {
    ssid:"My Home Network",
    security: "WEP",
    channel: 11,
    strength : -50
  }
</script>

<Meta title="Network" component={Network}/>

<Template let:args>
  <Network {...args}/>
</Template>

<Story name="Primary" args={defaults}/>

<Story name="Low Signal" args={{...defaults, strength: -90}}/>