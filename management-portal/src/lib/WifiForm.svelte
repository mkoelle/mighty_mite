<script lang="ts">
    import { Field, Input, Button } from "svelte-chota";
    let network, pass="";
</script>

<form name="setNetwork" action="#">
    <h2>WiFi connections</h2>

    <Field label="Network SSID" >
        <Input id="network" placeholder="My Home Network" bind:network/>
    </Field>
    
    <Field label="Password" >
        <Input id="password" password bind:pass/>
    </Field>
    <br />
    <Button submit>Submit</Button>
</form>
