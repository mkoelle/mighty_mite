<script>
  import { Meta, Template, Story } from '@storybook/addon-svelte-csf';
  import Network from './Network.svelte';
</script>

<Meta title="Network" component={Network}/>

<Template let:args>
  <Network {...args}/>
</Template>

<Story name="Primary" args={{primary: true}}/>

<Story name="Secondary" args={{primary: false}}/>