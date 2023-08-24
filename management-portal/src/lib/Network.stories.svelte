<script>
  import { Meta, Template, Story } from '@storybook/addon-svelte-csf';
  import Network from './Network.svelte';
  let defaults = {
    SSID:"My Home Network",
    Security: "My Home Network",
    Strength : -50
  }
</script>

<Meta title="Network" component={Network}/>

<Template let:args>
  <Network {...args}/>
</Template>

<Story name="Primary" args={defaults}/>

<Story name="Low Signal" args={{...defaults, Strength: -90}}/>