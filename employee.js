class Employee {
    constructor(employeeName, department, netPay) {
        this.employeeName = employeeName;
        this.department = department;
        this.netPay = netPay;
    }
 
    toString() {
        return `Employee{name='${this.employeeName}', department='${this.department}', netPay=${this.netPay}}`;
    }
}
 
module.exports = Employee;