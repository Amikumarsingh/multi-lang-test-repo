import { User, UserManager, validateUser, formatUserData } from '../typescript/user_manager';

describe('UserManager', () => {
    test('should create user', () => {
        const manager = new UserManager();
        const user = manager.createUser('John', 'john@test.com');
        expect(user).toBeDefined();
    });

    test('should validate user', () => {
        const user: User = { name: 'John', email: 'john@test.com', age: 25 };
        expect(validateUser(user)).toBe(true);
    });

    test('should format user data', () => {
        const user: User = { name: 'John', email: 'john@test.com', age: 25 };
        const result = formatUserData(user);
        expect(result).toContain('John');
    });
});
