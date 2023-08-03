import { render, screen } from '@testing-library/svelte'
import App from './App.svelte'


describe("App", () => {
    it("renders", async () => {
        // Arrange
        
        // Act
        render(App)
        // Assert
        const form = await screen.findByText('Mighty Mite')
        expect(form).toBeTruthy()
    });

    it("has a counter", async () => {
        // Arrange

        // Act
        render(App)
        // Assert
        const form = await screen.findByText('count is 0')
        expect(form).toBeTruthy()
    });

    it("has a wifi form", async () => {
        // Arrange

        // Act
        render(App)
        // Assert
        const form = await screen.findByText('WiFi connections')
        expect(form).toBeTruthy()
    });
});

